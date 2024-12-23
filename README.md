
## BetterTherapy: Empowering Personalized Mental Health Solutions  

[**BetterTherapy.AI**]("https://bettertherapy.ai/) is the most affordable mental healthcare platform leveraging the power of digital AI twin doctors. It incentivizes real doctors, health professionals, and even patients through the tokenization of “therapy” sessions and also builds a network of personalized mental health markets, focusing on user-centric therapy models across the following applications:  
- Personalized Mental Health Plans: AI-generated therapy plans tailored to individual needs.  
- Resource Marketplaces: Curated digital tools, articles, and interactive exercises for mental health management.  
- Peer Support Community: Connect users with similar experiences for mutual growth and understanding.  
- Predictive Emotional Analytics: AI-powered insights into emotional trends and potential mental health challenges.   

---

Current Phase: Distributed LLM Fine-Tuning with Ray
We are in Phase 1, utilizing Ray, a powerful library for distributed computation, to manage and distribute tasks across all participating nodes (miners). These tasks focus on fine-tuning large language models (LLMs) and processing unstructured data.

Key Libraries in Use
Ray Data: For distributed and unstructured data processing to prepare training datasets efficiently.
Ray Train: To scale model fine-tuning across multiple nodes.

#### Tasks for Contributors  

For Miners:  
1. Contribute Hardware Resources: Provide computational power to execute tasks distributed via Ray (CPU, GPU, RAM, Bandwidth, Storage).
2. Keep being updated and be ready for instant changes needed according to tasks needed to be done

For Validators:  
1. Evaluate Miner Responses: Assign scores based on the total resources contributed by miners. 
2. More the quantity and quality of resources more the rewards. 

---

### Getting Started with BetterTherapy  

#### 1. Setting Up the Project  
1. Clone the Repository:  
   ```bash
   git clone https://github.com/Better-Therapy/commune-subnet
   cd commune-subnet 
   ```  
2. Install Dependencies:  
   ```bash
   poetry install  
   ```  

#### 2. Wallet Setup  
Create and fund your wallet using the Commune CLI:  
```bash
comx key create <key_name>  
```  

#### 4. Register Your Module  

Miner Registration:  
```bash
comx module register <name> <your_commune_key> --ip <your-ip-address> --port <port> --netuid <Bettertherapy netuid>  
```  

Validator Registration:  
```bash
comx module register <name> <your_commune_key> --netuid <Bettertherapy netuid>  
```  

---

### Running the Miner  

1. Launch the miner:  
   - Make sure you get a GPU/CPU device on cloud or you can even port forward your device to public IP
   - Install `python 3.10.12` and Ray using `pip install -U "ray[data,train,tune,serve]` make sure the ray version is 2.40.0
   - Connect to master node using the following command(make sure you have enough external/internal ports available) Number of required free ports : 10+ 2 x (no.of CPU + no.of GPU)
      `ray start --address='188.166.188.104:6379' --node-ip-address="your-ip-address" --node-manage-port="your port specified while registering module"`
   - make sure your ip address and port matches with the one that you used while registering module to our subnet
   - once you are connected to ray, you are good to go
   

### Running the Validator  

#### Install and Run Using Script
`chmod +x run_btai_vali.sh`
`./run_btai_vali.sh`

#### Run Using script
Make sure you are inside commune-subnet directory
`chmod +x run_vali.sh`
`./run_vali.sh`

#### Run Step by Step

1. Update `_config.py` with dashboard api and other subnet constants. (For now default the recommended config)  
2. Run the validator script:  
   ```bash
   poetry shell  
   poetry run python -m src.betterTherapy.cli 
   ```  

---

Join Us and Grow with #BetterTherapy  
At BetterTherapy, we aim to redefine mental health support by combining advanced AI with the power of human insight. Together, we can create a more compassionate and effective approach to well-being.
