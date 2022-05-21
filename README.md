# Setup

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Install [Algorand sandbox](https://github.com/algorand/sandbox)
3. Add this project folder as bind volume in sandbox `docker-compose.yml` under key `services.algod`:
   ```yml
   volumes:
     - type: bind
       source: <path>
       target: /data
   ```
4. Start sandbox:
   ```txt
   $ ./sandbox up
   ```
5. Install Python virtual environment in project folder:
   ```txt
   $ python3 -m venv venv
   $ source ./venv/Scripts/activate # Windows
   $ source ./venv/bin/activate # Linux
   ```
6. Use Python interpreter: `./venv/Scripts/python.exe`
   VSCode: `Python: Select Interpreter`

# Links

- [Official Algorand Smart Contract Guidelines](https://developer.algorand.org/docs/get-details/dapps/avm/teal/guidelines/)
- [PyTeal Documentation](https://pyteal.readthedocs.io/en/latest/index.html)
- [Algorand DevRel Example Contracts](https://github.com/algorand/smart-contracts)

Youtube: https://www.youtube.com/watch?v=w1eYtAR5brY

### Compile

```
./build.sh contracts.rps.step_01
```

## Counter Contract

```
// Deploy Contract
goal app create --creator $ONE --approval-prog /data/build/approval.teal --clear-prog /data/build/clear.teal --global-byteslices 1 --global-ints 1 --local-byteslices 0 --local-ints 0

// Change Contract State
// increment:
goal app call --app-id 1 --from $ONE --app-arg "str:inc"

// decrement:
goal app call --app-id 7 --from $ONE --app-arg "str:dec"

// Read Contract Storage
goal app read --global --app-id 1 --guess-format

```

## Rock Paper Scissors Contract

```
// Deploy Contract
goal app create --creator $ONE --approval-prog /data/build/approval.teal --clear-prog /data/build/clear.teal --global-byteslices 0 --global-ints 0 --local-byteslices 3 --local-ints 1
```
