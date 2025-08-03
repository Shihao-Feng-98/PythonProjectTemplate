import logging
import logging.handlers
import colorlog
from pathlib import Path
import threading
from datetime import datetime

__all__ = ["get_logger"]

PACKAGE_NAME = "pypjt"
LOG_DIR = Path.home() / f".{PACKAGE_NAME}" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)


def get_logger() -> logging.Logger:
    return Logger.get_instance()


LEVEL_COLORS = {
    "DEBUG": "blue",
    "INFO": "green",
    "WARNING": "yellow",
    "ERROR": "red",
    "CRITICAL": "red",
}


class Logger:
    class BaseMicroSecondFormatter:
        def formatTime(self, record, datefmt=None):
            dt = datetime.fromtimestamp(record.created)
            if datefmt:
                return dt.strftime(datefmt) + f",{dt.microsecond // 1000:03d}"
            else:
                return dt.strftime("%Y-%m-%d %H:%M:%S")

    class MicroSecondColoredFormatter(
        BaseMicroSecondFormatter, colorlog.ColoredFormatter
    ):
        pass

    class MicroSecondFormatter(BaseMicroSecondFormatter, logging.Formatter):
        pass

    _instance = None
    _lock = threading.Lock()

    @classmethod
    def get_instance(cls) -> logging.Logger:
        return cls(LOG_DIR / f"{PACKAGE_NAME}.log", PACKAGE_NAME)._logger

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, log_file_path="", name="root"):
        if hasattr(self, "_initialized") and self._initialized:
            return
        self._initialized = True

        self._log_file_path = Path(log_file_path)

        log_dir = self._log_file_path.parent
        if not log_dir.exists():
            log_dir.mkdir(parents=True, exist_ok=True)

        self._logger = logging.getLogger(name)
        self._logger.setLevel(logging.DEBUG)

        for handler in self._logger.handlers[:]:
            self._logger.removeHandler(handler)

        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(logging.DEBUG)  # Modify as you need
        self.console_handler.setFormatter(
            self.MicroSecondColoredFormatter(
                "[%(asctime)s] [%(name)s] [%(log_color)s%(levelname)s%(light_white)s] [%(filename)s:%(lineno)d]: %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
                log_colors=LEVEL_COLORS,
            )
        )

        self.file_handler = logging.handlers.RotatingFileHandler(
            filename=self._log_file_path,
            maxBytes=104856700,
            backupCount=20,
            encoding="utf8",
        )
        self.file_handler.setLevel(logging.DEBUG)  # Modify as you need
        self.file_handler.setFormatter(
            self.MicroSecondFormatter(
                "[%(asctime)s] [%(name)s] [%(levelname)s] [%(filename)s-%(lineno)d line]: %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
        )

        self._logger.addHandler(self.console_handler)
        self._logger.addHandler(self.file_handler)


if __name__ == "__main__":
    pypj_logger = get_logger()

    pypj_logger.debug("debug")
    pypj_logger.info("info")
    pypj_logger.warning("warning")
    pypj_logger.error("error")
    pypj_logger.critical("critical")
