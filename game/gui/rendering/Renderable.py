from abc import ABCMeta, abstractmethod


class Renderable:
	__metaclass__ = ABCMeta

	@abstractmethod
	def update(self):
		raise NotImplementedError

	@property
	@abstractmethod
	def pygletObject(self):
		raise NotImplementedError
