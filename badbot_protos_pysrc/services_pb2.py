# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import message_pb2 as message__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='services.proto',
  package='badbot.messages',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0eservices.proto\x12\x0f\x62\x61\x64\x62ot.messages\x1a\rmessage.proto\x1a\x1bgoogle/protobuf/empty.proto2\xa0\x01\n\nBotService\x12\x45\n\x0eprocessCommand\x12\x1b.badbot.messages.BadMessage\x1a\x16.google.protobuf.Empty\x12K\n\x12subscribeToUpdates\x12\x16.google.protobuf.Empty\x1a\x1b.badbot.messages.BadMessage0\x01\x62\x06proto3'
  ,
  dependencies=[message__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_BOTSERVICE = _descriptor.ServiceDescriptor(
  name='BotService',
  full_name='badbot.messages.BotService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=80,
  serialized_end=240,
  methods=[
  _descriptor.MethodDescriptor(
    name='processCommand',
    full_name='badbot.messages.BotService.processCommand',
    index=0,
    containing_service=None,
    input_type=message__pb2._BADMESSAGE,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='subscribeToUpdates',
    full_name='badbot.messages.BotService.subscribeToUpdates',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=message__pb2._BADMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BOTSERVICE)

DESCRIPTOR.services_by_name['BotService'] = _BOTSERVICE

# @@protoc_insertion_point(module_scope)
