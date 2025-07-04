# Dadabot website
## Deployment
Dependencies are installed automatically. Make sure that you have [docker](https://www.docker.com/) and installed on your system. Check that you have the databot-data directory in your project. Then, run the following commands from the root of the project, but modify the path to point to the databot-data directory.

```
export DADABOT_DATA_PATH=/path/to/dadabot-data
docker compose build
docker compose up
```