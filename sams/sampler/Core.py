"""
Saves core information about a job from the collector command line options.
"""
import sams.base

import logging
logger = logging.getLogger(__name__)

class Sampler(sams.base.Sampler):
    core = None

    def do_sample(self):
        return self.core is None

    def sample(self):
        logger.debug("sample()")

        self.core = {
            'jobid': self.config.get(['options','jobid']),
            'node': self.config.get(['options','node']),
        }

        self.store(self.core)

    def final_data(self):
        return self.core
