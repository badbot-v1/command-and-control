# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: videoframe.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='videoframe.proto',
  package='badbot.messages',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10videoframe.proto\x12\x0f\x62\x61\x64\x62ot.messages\"L\n\nVideoFrame\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\x12\x10\n\x08\x63hannels\x18\x03 \x01(\r\x12\r\n\x05\x66rame\x18\x04 \x01(\x0c\x62\x06proto3'
)




_VIDEOFRAME = _descriptor.Descriptor(
  name='VideoFrame',
  full_name='badbot.messages.VideoFrame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='badbot.messages.VideoFrame.width', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='badbot.messages.VideoFrame.height', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channels', full_name='badbot.messages.VideoFrame.channels', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frame', full_name='badbot.messages.VideoFrame.frame', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=113,
)

DESCRIPTOR.message_types_by_name['VideoFrame'] = _VIDEOFRAME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VideoFrame = _reflection.GeneratedProtocolMessageType('VideoFrame', (_message.Message,), {
  'DESCRIPTOR' : _VIDEOFRAME,
  '__module__' : 'videoframe_pb2'
  # @@protoc_insertion_point(class_scope:badbot.messages.VideoFrame)
  })
_sym_db.RegisterMessage(VideoFrame)


# @@protoc_insertion_point(module_scope)
