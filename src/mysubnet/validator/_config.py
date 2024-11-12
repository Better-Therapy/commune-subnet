from pydantic_settings import BaseSettings


class ValidatorSettings(BaseSettings):
    # == Scoring ==
    iteration_interval: int = 800  # Set, accordingly to your tempo.
    max_allowed_weights: int = 400  # Query dynamically based on your subnet settings.
    dashboard_api_url: str = "http://142.120.191.128:50923/nodes?view=summary"  # The URL of the dashboard API.
