from dataclasses import dataclass


@dataclass
class Location:
    longitude: float
    latitude: float
@dataclass
class Stop:
    id: str
    name: str
    location: Location
    tracks: bool = False
@dataclass
class Route:
    id: str
    name: str
    stops: list[Stop]

@dataclass
class Constants:
    MUNI_PROVIDER_ID = "SF"
    N_OB: Route = Route(
        id="N",
        name="JUDAH",
        stops=[
            # N Carl & Cole Towards OB
            Stop(
                id="13909",
                name="Carl St & Cole St",
                location=Location(
                    longitude=-122.449804,
                    latitude=37.765863
                ),
                tracks=True
            ),
            # N Carl & Cole Towards CalTrain
            Stop(
                id="13911",
                name="Carl St & Cole St",
                location=Location(
                    longitude=-122.450131,
                    latitude=37.765745
                ),
                tracks=True
            ),
        ]
    )