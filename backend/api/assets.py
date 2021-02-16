from dataclasses import dataclass


@dataclass
class AssetItem:
    id: int
    code: str
    tags: list[str]
    imageURI: str
    projectID: int
