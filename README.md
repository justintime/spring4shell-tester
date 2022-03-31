# spring4shell-tester
Tests for spring4shell vulnerability

## What this is
It's a modified version of the PoC code that was initially released on 3/30/2022, but it's been de-weaponized.  Rather than dropping a webshell, it drops a random text file and then checks to see if it can be retreived.

## Testing the tester
If you want to make things easy, use docker to pull down `vulfocus/spring-core-rce-2022-03-29`  Start it up and then run:
```
python3 spring4shell-test.py --url http://localhost:8080
```

## Observations
This does not work reliably every time.  If it's not working, restart the container and try again.  I'm not positive, but I think that doing a `curl http://localhost:8080` before running the python script produces slightly better results.
