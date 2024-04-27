import pytest
from httpx import AsyncClient
from main import app


@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url='http://test/api/balance') as c:
        yield c


class TestAPIService:
    base_url = 'http://test/api/balance'

    @pytest.mark.parametrize('params', [
        {'identifier': 1, 'amount': 100},
        {'identifier': 2, 'amount': 200.50},
        {'identifier': 3, 'amount': 374}
    ])
    async def test_replenishment_endpoint(self, params, client):
        response = await client.post('/replenishment/', params=params)
        assert response.status_code == 200
        assert response.json() == {
            'message': f'Replenishment for user with ID: ({params["identifier"]}) has been successfully completed.'
        }

    @pytest.mark.parametrize('params', [
        {'identifier': 4, 'amount': 111},
        {'identifier': 6, 'amount': 444.44},
        {'identifier': 9, 'amount': 222.222}
    ])
    async def test_withdraw_endpoint(self, params, client):
        response = await client.post('/withdraw/', params=params)
        assert response.status_code == 200

    @pytest.mark.parametrize('params', [
        {'sender_id': 7, 'receiver_id': 10, 'amount': 123},
        {'sender_id': 3, 'receiver_id': 5, 'amount': 11},
        {'sender_id': 2, 'receiver_id': 8, 'amount': 2.7}
    ])
    async def test_transfer_endpoint(self, params, client):
        response = await client.post('/transfer/', params=params)
        assert response.status_code == 200

    @pytest.mark.parametrize('params', [
        {'identifier': 1},
        {'identifier': 7},
        {'identifier': 2}
    ])
    async def test_getting_endpoint(self, params, client):
        response = await client.get('/', params=params)
        assert response.status_code == 200

