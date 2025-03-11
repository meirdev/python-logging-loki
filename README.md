# Example: Python logging to Loki

Send logs from Python to Loki with Alloy.

## Log rotation

To rotate the log file, you can use `logging.handlers.RotatingFileHandler` but for this example I'm using `logrotate`.

Copy the file `./logrotate/app` to `/etc/logrotate.d/` and change the path (`/path/to/log/file`) to the full path of the log file.

```bash
sudo cp logrotate/app /etc/logrotate.d/
```
