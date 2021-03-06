# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: consts.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='consts.proto',
  package='badbot.messages',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x63onsts.proto\x12\x0f\x62\x61\x64\x62ot.messages*\xf6\x01\n\x0bMessageType\x12\x0e\n\nSTATUS_BOT\x10\x00\x12\x0e\n\nCMD_TOGGLE\x10\x01\x12\x18\n\x14\x43MD_OPERATIONAL_MODE\x10\x02\x12\x17\n\x13\x43MD_TELEOP_MOVEMENT\x10\x03\x12\x10\n\x0cHEARTBEAT_RC\x10\x04\x12\x0f\n\x0bVIDEO_FRAME\x10\x05\x12\x0c\n\x08TELE_IMU\x10\x06\x12\x0e\n\nTELE_LIDAR\x10\x07\x12\x0c\n\x08TELE_GPS\x10\x08\x12\x16\n\x12VPM_OBJ_DET_COORDS\x10\t\x12\x19\n\x15TELE_DRIVELINE_STATUS\x10\n\x12\x12\n\x0eTELE_LIDAR_POI\x10\x0b*F\n\x0fOperationalMode\x12\n\n\x06TELEOP\x10\x00\x12\r\n\tFOLLOW_ME\x10\x01\x12\x0e\n\nAUTONOMOUS\x10\x02\x12\x08\n\x04IDLE\x10\x04*\x96\x01\n\x07\x44\x65vices\x12\t\n\x05LIDAR\x10\x00\x12\x10\n\x0cLIDAR_RECORD\x10\x01\x12\n\n\x06\x41PPSRC\x10\x02\x12\x0b\n\x07\x41PPSINK\x10\x03\x12\r\n\tDRIVELINE\x10\x04\x12\x13\n\x0fVISUALTELEMETRY\x10\x05\x12\x0c\n\x08WS_VIDEO\x10\x06\x12\r\n\tTELEMETRY\x10\x07\x12\x14\n\x10OBJECT_DETECTION\x10\x08\x62\x06proto3'
)

_MESSAGETYPE = _descriptor.EnumDescriptor(
  name='MessageType',
  full_name='badbot.messages.MessageType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_BOT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD_TOGGLE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD_OPERATIONAL_MODE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD_TELEOP_MOVEMENT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HEARTBEAT_RC', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_FRAME', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TELE_IMU', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TELE_LIDAR', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TELE_GPS', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VPM_OBJ_DET_COORDS', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TELE_DRIVELINE_STATUS', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TELE_LIDAR_POI', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=34,
  serialized_end=280,
)
_sym_db.RegisterEnumDescriptor(_MESSAGETYPE)

MessageType = enum_type_wrapper.EnumTypeWrapper(_MESSAGETYPE)
_OPERATIONALMODE = _descriptor.EnumDescriptor(
  name='OperationalMode',
  full_name='badbot.messages.OperationalMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TELEOP', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FOLLOW_ME', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AUTONOMOUS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IDLE', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=282,
  serialized_end=352,
)
_sym_db.RegisterEnumDescriptor(_OPERATIONALMODE)

OperationalMode = enum_type_wrapper.EnumTypeWrapper(_OPERATIONALMODE)
_DEVICES = _descriptor.EnumDescriptor(
  name='Devices',
  full_name='badbot.messages.Devices',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LIDAR', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LIDAR_RECORD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='APPSRC', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='APPSINK', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DRIVELINE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VISUALTELEMETRY', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WS_VIDEO', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TELEMETRY', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OBJECT_DETECTION', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=355,
  serialized_end=505,
)
_sym_db.RegisterEnumDescriptor(_DEVICES)

Devices = enum_type_wrapper.EnumTypeWrapper(_DEVICES)
STATUS_BOT = 0
CMD_TOGGLE = 1
CMD_OPERATIONAL_MODE = 2
CMD_TELEOP_MOVEMENT = 3
HEARTBEAT_RC = 4
VIDEO_FRAME = 5
TELE_IMU = 6
TELE_LIDAR = 7
TELE_GPS = 8
VPM_OBJ_DET_COORDS = 9
TELE_DRIVELINE_STATUS = 10
TELE_LIDAR_POI = 11
TELEOP = 0
FOLLOW_ME = 1
AUTONOMOUS = 2
IDLE = 4
LIDAR = 0
LIDAR_RECORD = 1
APPSRC = 2
APPSINK = 3
DRIVELINE = 4
VISUALTELEMETRY = 5
WS_VIDEO = 6
TELEMETRY = 7
OBJECT_DETECTION = 8


DESCRIPTOR.enum_types_by_name['MessageType'] = _MESSAGETYPE
DESCRIPTOR.enum_types_by_name['OperationalMode'] = _OPERATIONALMODE
DESCRIPTOR.enum_types_by_name['Devices'] = _DEVICES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
