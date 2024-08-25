Test automation task for GEN gen-task-python
===========================================

## How to use:
### Installation
0. Clone repository
1. Install Python 3.11 from official site - (https://www.python.org/downloads/)
2. Create venv dir inside project with command:
```sh
python3 -m venv venv
```
3. Activate venv:<br>
on Windows:
```sh
.\venv\Scripts\activate
```
on MacOS/Linux:
```sh
source venv/bin/activate
```
4. Install project packages:
```sh
python3 -m pip install -r requirements.txt
```
5. Install browsers:
```sh
playwright install
```

### Run test
To run test on Windows use:
```sh
pytest -s .\tests\test_room_booking.py
```
on MacOS, Linux:
```sh
pytest -s ./tests/test_room_booking.py
```
