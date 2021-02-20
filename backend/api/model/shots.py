from dataclasses import dataclass


@dataclass
class ShotItem:
    id: int
    code: str
    sequence: str
    projectID: int
    cut: list[int]
    bufferFrames: int
    movieURI: str
    assetList: dict[str, int]
