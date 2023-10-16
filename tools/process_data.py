import os
from loguru import logger

from data_juicer.config import init_configs
from data_juicer.core import Executor

@logger.catch
def main():
    cfg = init_configs()
    executor = None
    if cfg.executor_type == 'default':
        executor = Executor(cfg)
    elif cfg.executor_type == 'ray':
        # https://github.com/alibaba/data-juicer/issues/30
        # Ray 框架在没有分布式系统的情况下，不要import使用
        from data_juicer.core import RayExecutor
        executor = RayExecutor(cfg)
    assert executor is not None, f"didn't specify executor type, choose between [default, ray]"
    executor.run()


if __name__ == '__main__':
    main()
