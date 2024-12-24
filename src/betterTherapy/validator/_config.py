from pydantic_settings import BaseSettings


class ValidatorSettings(BaseSettings):
    # == Scoring ==
    iteration_interval: int = 700  # Set, accordingly to your tempo.
    max_allowed_weights: int = 420  # Query dynamically based on your subnet settings.
    dashboard_api_url: str = (
        "http://188.166.188.104:8265/nodes?view=summary"  # The URL of the dashboard API.
    )
    subnet_netuid: int = 34
    use_testnet: bool = False
