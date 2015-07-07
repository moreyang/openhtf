# Copyright 2014 Google Inc. All Rights Reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""One-off utilities."""

import logging
import time


def LogEveryNToLogger(n, logger, level, message, *args):
  """Logs the given message every n calls to a logger.

  Args:
    n: Number of calls before logging.
    logger: The logger to which to log.
    level: The logging level (e.g. logging.INFO).
    message: A message to log
    *args: Any format args for the message.
  Returns:
    A method that logs and returns True every n calls.
  """
  logger = logger or logging.getLogger()
  def _Gen():
    while True:
      for _ in xrange(n):
        yield False
      logger.log(level, message, *args)
      yield True
  g = _Gen()
  return lambda: next(g)


def LogEveryN(n, level, message, *args):
  """Logs a message every n calls. See LogEveryNToLogger."""
  return LogEveryNToLogger(n, None, level, message, *args)


def TimeMillis():
  """The time in milliseconds."""
  return int(time.time() * 1000)
