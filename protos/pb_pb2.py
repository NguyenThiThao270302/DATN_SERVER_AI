# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pb.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08pb.proto\x12\x06\x61ipool\"\x1f\n\tAIRequest\x12\x12\n\ninput_data\x18\x01 \x01(\t\"C\n\nAIResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x13\n\x0boutput_data\x18\x03 \x01(\t2F\n\tAIService\x12\x39\n\x10ProcessAIRequest\x12\x11.aipool.AIRequest\x1a\x12.aipool.AIResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pb_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_AIREQUEST']._serialized_start=20
  _globals['_AIREQUEST']._serialized_end=51
  _globals['_AIRESPONSE']._serialized_start=53
  _globals['_AIRESPONSE']._serialized_end=120
  _globals['_AISERVICE']._serialized_start=122
  _globals['_AISERVICE']._serialized_end=192
# @@protoc_insertion_point(module_scope)
