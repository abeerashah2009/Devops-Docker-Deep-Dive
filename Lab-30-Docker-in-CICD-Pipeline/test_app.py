import app

def test_counter_increments():
    client = app.app.test_client()
    first = int(client.get("/").data.decode().split()[1])
    second = int(client.get("/").data.decode().split()[1])
    assert second == first + 1
