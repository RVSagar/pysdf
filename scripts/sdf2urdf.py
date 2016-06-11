#!/usr/bin/env python
import sys
import pysdf


def main():
  sdf = pysdf.SDF(sys.argv[1])
  world = sdf.world
  if len(world.models) != 1:
    print('SDF contains %s instead of exactly one model. Aborting.' % len(world.models))
    sys.exit(1)

  model = world.models[0]
  #print(model)
  model.save_urdf(sys.argv[2])


if __name__ == '__main__':
  main()
