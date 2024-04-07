import platform


def parse_host(host: str):
    match platform:
        case "Linux" | "Darwin":
            if host == "localhost":
                host = "0.0.0.0"
        case "Windows":
            if host == "0.0.0.0":
                host = "localhost"
    return host
