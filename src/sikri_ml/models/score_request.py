class ScoreRequest:
    text: str

    def __init__(self, text: str):
        self.text = text


def score_request_decoder(fields: dict) -> ScoreRequest:
    return ScoreRequest(**fields)
