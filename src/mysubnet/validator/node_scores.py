import requests

# GPU capability scores based on relative performance
gpu_scores = {
    "NVIDIA A100": 10,
    "NVIDIA A40": 9.5,
    "NVIDIA A30": 9.0,
    "NVIDIA V100": 8.5,
    "NVIDIA T4": 7.5,
    "NVIDIA P100": 7.0,
    "NVIDIA K80": 5.5,
    "NVIDIA RTX A6000": 9.0,
    "NVIDIA RTX A5000": 8.5,
    "NVIDIA RTX A4000": 8.0,
    "NVIDIA RTX A2000": 7.0,
    "NVIDIA Quadro RTX 8000": 8.5,
    "NVIDIA Quadro RTX 6000": 8.0,
    "NVIDIA Quadro P6000": 7.5,
    "NVIDIA Quadro P5000": 6.5,
    "NVIDIA RTX 3090": 8.0,
    "NVIDIA RTX 3080 Ti": 7.5,
    "NVIDIA RTX 3080": 7.0,
    "NVIDIA RTX 3070 Ti": 6.5,
    "NVIDIA RTX 3070": 6.0,
    "NVIDIA GTX 1080 Ti": 5.5,
    "NVIDIA GTX 1080": 5.0,
    "NVIDIA GTX 1070": 4.5,
}


def get_gpu_score(gpu_name):
    """Return the GPU score if the model is recognized, else default to a low score."""
    return gpu_scores.get(gpu_name, 2.0)  # Default score for unlisted GPUs


def calculate_node_score(node):
    """Calculate the resource-based score for a single node."""
    # Weights for each resource
    weights = {"cpu": 0.2, "memory": 0.2, "disk": 0.1, "network": 0.1, "gpu": 0.4}

    # CPU Score
    total_cpus = node["cpus"][0]
    cpu_utilization = node["agent"]["cpuPercent"]
    available_cpu = total_cpus * (1 - cpu_utilization / 100)
    cpu_score = (available_cpu / total_cpus) * weights["cpu"]

    # Memory Score
    total_memory = node["mem"][0]
    used_memory = node["mem"][1]
    available_memory = total_memory - used_memory
    memory_score = (available_memory / total_memory) * weights["memory"]

    # Disk Score
    total_disk_space = node["disk"]["/"]["total"]
    available_disk_space = node["disk"]["/"]["free"]
    disk_score = (available_disk_space / total_disk_space) * weights["disk"]

    # Network Score
    network_speed_upload = node["networkSpeed"][0]
    network_speed_download = node["networkSpeed"][1]
    average_network_speed = (network_speed_upload + network_speed_download) / 2
    max_network_speed = 5000  # Set based on typical max speed
    network_score = (average_network_speed / max_network_speed) * weights["network"]

    # GPU Score
    if "gpus" in node and len(node["gpus"]) > 0:
        gpu_name = node["gpus"][0]["name"]
        gpu_capability_score = get_gpu_score(gpu_name)
        gpu_utilization = (
            node["gpus"][0]["utilizationGpu"] / 100
        )  # Utilization as a fraction
        available_gpu = gpu_capability_score * (1 - gpu_utilization)
        gpu_score = (available_gpu / gpu_capability_score) * weights["gpu"]
    else:
        gpu_score = 0  # No GPU data available

    # Final Score Calculation
    node_score = cpu_score + memory_score + disk_score + network_score + gpu_score
    return node_score


def process_node_data(nodes):
    """Process a list of nodes, compute scores, and uniquely identify each node."""
    node_scores = []

    for node in nodes:
        # Create a unique identifier using IP and nodeManagerPort
        unique_id = f"{node['ip']}:{node['raylet']['nodeManagerPort']}"

        # Calculate the node's resource-based score
        score = calculate_node_score(node)

        # Append to the list with unique identifier and score
        node_scores.append({"node_id": unique_id, "score": score})

    return node_scores


def get_node_scores(url: str):
    node_data = requests.get(url)
    response_body = node_data.json()
    scores = process_node_data(response_body["data"]["summary"])
    return scores
