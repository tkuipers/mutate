#!/usr/bin/env python

from cleo.application import Application

from cmd.mutate_command import MutateCommand

application = Application()
application.add(MutateCommand())

if __name__ == "__main__":
  application.run()
