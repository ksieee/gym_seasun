# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='state.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0bstate.proto\"\xa1\x05\n\x05State\x12\x1d\n\x06player\x18\x01 \x01(\x0b\x32\r.State.Player\x12\x17\n\x03npc\x18\x02 \x03(\x0b\x32\n.State.Npc\x12\x1d\n\x06screen\x18\x03 \x01(\x0b\x32\r.State.Screen\x1a`\n\x06Screen\x12\x14\n\x0cmin_screen_x\x18\x01 \x01(\x02\x12\x14\n\x0cmax_screen_x\x18\x02 \x01(\x02\x12\x14\n\x0cmin_screen_y\x18\x03 \x01(\x02\x12\x14\n\x0cmax_screen_y\x18\x04 \x01(\x02\x1a\xf5\x01\n\x03Npc\x12\n\n\x02id\x18\x01 \x01(\x02\x12\x0f\n\x07temp_id\x18\x02 \x01(\x02\x12\t\n\x01x\x18\x03 \x01(\x02\x12\t\n\x01y\x18\x04 \x01(\x02\x12\x12\n\nmove_speed\x18\x05 \x01(\x02\x12\x0f\n\x07\x66\x61\x63\x65_to\x18\x06 \x01(\x05\x12\n\n\x02hp\x18\x07 \x01(\x02\x12\x0c\n\x04hp_m\x18\x08 \x01(\x02\x12\n\n\x02mp\x18\t \x01(\x02\x12\x0c\n\x04mp_m\x18\n \x01(\x02\x12\n\n\x02\x65p\x18\x0b \x01(\x02\x12\x0c\n\x04\x65p_m\x18\x0c \x01(\x02\x12\x0c\n\x04hp_v\x18\r \x01(\x02\x12\x0c\n\x04mp_v\x18\x0e \x01(\x02\x12\x0c\n\x04\x65p_v\x18\x0f \x01(\x02\x12\x10\n\x08relation\x18\x10 \x01(\x05\x12\x0c\n\x04type\x18\x11 \x01(\x05\x1a\xe6\x01\n\x06Player\x12\x18\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\n.State.Npc\x12#\n\x06skills\x18\x02 \x03(\x0b\x32\x13.State.Player.Skill\x1a\x9c\x01\n\x05Skill\x12\n\n\x02id\x18\x01 \x01(\x02\x12\x0c\n\x04type\x18\x02 \x01(\x05\x12\r\n\x05level\x18\x03 \x01(\x02\x12\r\n\x05range\x18\x04 \x01(\x02\x12\x0e\n\x06target\x18\x05 \x01(\x05\x12\x0c\n\x04\x63\x64_m\x18\x06 \x01(\x02\x12\n\n\x02\x63\x64\x18\x07 \x01(\x02\x12\x0f\n\x07hp_cost\x18\x08 \x01(\x02\x12\x0f\n\x07mp_cost\x18\t \x01(\x02\x12\x0f\n\x07\x65p_cost\x18\n \x01(\x02')
)




_STATE_SCREEN = _descriptor.Descriptor(
  name='Screen',
  full_name='State.Screen',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_screen_x', full_name='State.Screen.min_screen_x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_screen_x', full_name='State.Screen.max_screen_x', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_screen_y', full_name='State.Screen.min_screen_y', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_screen_y', full_name='State.Screen.max_screen_y', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=208,
)

_STATE_NPC = _descriptor.Descriptor(
  name='Npc',
  full_name='State.Npc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='State.Npc.id', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temp_id', full_name='State.Npc.temp_id', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='State.Npc.x', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='State.Npc.y', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move_speed', full_name='State.Npc.move_speed', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='face_to', full_name='State.Npc.face_to', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hp', full_name='State.Npc.hp', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hp_m', full_name='State.Npc.hp_m', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mp', full_name='State.Npc.mp', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mp_m', full_name='State.Npc.mp_m', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ep', full_name='State.Npc.ep', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ep_m', full_name='State.Npc.ep_m', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hp_v', full_name='State.Npc.hp_v', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mp_v', full_name='State.Npc.mp_v', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ep_v', full_name='State.Npc.ep_v', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relation', full_name='State.Npc.relation', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='State.Npc.type', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=456,
)

_STATE_PLAYER_SKILL = _descriptor.Descriptor(
  name='Skill',
  full_name='State.Player.Skill',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='State.Player.Skill.id', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='State.Player.Skill.type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='State.Player.Skill.level', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='range', full_name='State.Player.Skill.range', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target', full_name='State.Player.Skill.target', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cd_m', full_name='State.Player.Skill.cd_m', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cd', full_name='State.Player.Skill.cd', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hp_cost', full_name='State.Player.Skill.hp_cost', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mp_cost', full_name='State.Player.Skill.mp_cost', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ep_cost', full_name='State.Player.Skill.ep_cost', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=533,
  serialized_end=689,
)

_STATE_PLAYER = _descriptor.Descriptor(
  name='Player',
  full_name='State.Player',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base', full_name='State.Player.base', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skills', full_name='State.Player.skills', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_STATE_PLAYER_SKILL, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=459,
  serialized_end=689,
)

_STATE = _descriptor.Descriptor(
  name='State',
  full_name='State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player', full_name='State.player', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='npc', full_name='State.npc', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='screen', full_name='State.screen', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_STATE_SCREEN, _STATE_NPC, _STATE_PLAYER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=689,
)

_STATE_SCREEN.containing_type = _STATE
_STATE_NPC.containing_type = _STATE
_STATE_PLAYER_SKILL.containing_type = _STATE_PLAYER
_STATE_PLAYER.fields_by_name['base'].message_type = _STATE_NPC
_STATE_PLAYER.fields_by_name['skills'].message_type = _STATE_PLAYER_SKILL
_STATE_PLAYER.containing_type = _STATE
_STATE.fields_by_name['player'].message_type = _STATE_PLAYER
_STATE.fields_by_name['npc'].message_type = _STATE_NPC
_STATE.fields_by_name['screen'].message_type = _STATE_SCREEN
DESCRIPTOR.message_types_by_name['State'] = _STATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), dict(

  Screen = _reflection.GeneratedProtocolMessageType('Screen', (_message.Message,), dict(
    DESCRIPTOR = _STATE_SCREEN,
    __module__ = 'state_pb2'
    # @@protoc_insertion_point(class_scope:State.Screen)
    ))
  ,

  Npc = _reflection.GeneratedProtocolMessageType('Npc', (_message.Message,), dict(
    DESCRIPTOR = _STATE_NPC,
    __module__ = 'state_pb2'
    # @@protoc_insertion_point(class_scope:State.Npc)
    ))
  ,

  Player = _reflection.GeneratedProtocolMessageType('Player', (_message.Message,), dict(

    Skill = _reflection.GeneratedProtocolMessageType('Skill', (_message.Message,), dict(
      DESCRIPTOR = _STATE_PLAYER_SKILL,
      __module__ = 'state_pb2'
      # @@protoc_insertion_point(class_scope:State.Player.Skill)
      ))
    ,
    DESCRIPTOR = _STATE_PLAYER,
    __module__ = 'state_pb2'
    # @@protoc_insertion_point(class_scope:State.Player)
    ))
  ,
  DESCRIPTOR = _STATE,
  __module__ = 'state_pb2'
  # @@protoc_insertion_point(class_scope:State)
  ))
_sym_db.RegisterMessage(State)
_sym_db.RegisterMessage(State.Screen)
_sym_db.RegisterMessage(State.Npc)
_sym_db.RegisterMessage(State.Player)
_sym_db.RegisterMessage(State.Player.Skill)


# @@protoc_insertion_point(module_scope)
