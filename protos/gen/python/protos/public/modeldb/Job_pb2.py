# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/public/modeldb/Job.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos.public.common import CommonService_pb2 as protos_dot_public_dot_common_dot_CommonService__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/public/modeldb/Job.proto',
  package='ai.verta.modeldb',
  syntax='proto3',
  serialized_options=b'P\001Z>github.com/VertaAI/modeldb/protos/gen/go/protos/public/modeldb',
  serialized_pb=b'\n\x1fprotos/public/modeldb/Job.proto\x12\x10\x61i.verta.modeldb\x1a(protos/public/common/CommonService.proto\x1a\x1cgoogle/api/annotations.proto\"M\n\rJobStatusEnum\"<\n\tJobStatus\x12\x0f\n\x0bNOT_STARTED\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\r\n\tCOMPLETED\x10\x02\",\n\x0bJobTypeEnum\"\x1d\n\x07JobType\x12\x12\n\x0eKUBERNETES_JOB\x10\x00\"\x80\x02\n\x03Job\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x12\n\nstart_time\x18\x03 \x01(\t\x12\x10\n\x08\x65nd_time\x18\x04 \x01(\t\x12+\n\x08metadata\x18\x05 \x03(\x0b\x32\x19.ai.verta.common.KeyValue\x12=\n\njob_status\x18\x06 \x01(\x0e\x32).ai.verta.modeldb.JobStatusEnum.JobStatus\x12\x37\n\x08job_type\x18\x07 \x01(\x0e\x32%.ai.verta.modeldb.JobTypeEnum.JobType\x12\r\n\x05owner\x18\x08 \x01(\t\"\x9b\x02\n\tCreateJob\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\nstart_time\x18\x02 \x01(\t\x12\x10\n\x08\x65nd_time\x18\x03 \x01(\t\x12+\n\x08metadata\x18\x04 \x03(\x0b\x32\x19.ai.verta.common.KeyValue\x12=\n\njob_status\x18\x05 \x01(\x0e\x32).ai.verta.modeldb.JobStatusEnum.JobStatus\x12\x37\n\x08job_type\x18\x06 \x01(\x0e\x32%.ai.verta.modeldb.JobTypeEnum.JobType\x1a.\n\x08Response\x12\"\n\x03job\x18\x01 \x01(\x0b\x32\x15.ai.verta.modeldb.Job\"\x98\x01\n\tUpdateJob\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x65nd_time\x18\x03 \x01(\t\x12=\n\njob_status\x18\x02 \x01(\x0e\x32).ai.verta.modeldb.JobStatusEnum.JobStatus\x1a.\n\x08Response\x12\"\n\x03job\x18\x01 \x01(\x0b\x32\x15.ai.verta.modeldb.Job\"3\n\tDeleteJob\x12\n\n\x02id\x18\x01 \x01(\t\x1a\x1a\n\x08Response\x12\x0e\n\x06status\x18\x01 \x01(\x08\"D\n\x06GetJob\x12\n\n\x02id\x18\x01 \x01(\t\x1a.\n\x08Response\x12\"\n\x03job\x18\x01 \x01(\x0b\x32\x15.ai.verta.modeldb.Job2\xaf\x03\n\nJobService\x12l\n\tcreateJob\x12\x1b.ai.verta.modeldb.CreateJob\x1a$.ai.verta.modeldb.CreateJob.Response\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x11/v1/job/createJob:\x01*\x12]\n\x06getJob\x12\x18.ai.verta.modeldb.GetJob\x1a!.ai.verta.modeldb.GetJob.Response\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/v1/job/getJob\x12i\n\tupdateJob\x12\x1b.ai.verta.modeldb.UpdateJob\x1a$.ai.verta.modeldb.UpdateJob.Response\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/v1/job/updateJob\x12i\n\tdeleteJob\x12\x1b.ai.verta.modeldb.DeleteJob\x1a$.ai.verta.modeldb.DeleteJob.Response\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/v1/job/deleteJobBBP\x01Z>github.com/VertaAI/modeldb/protos/gen/go/protos/public/modeldbb\x06proto3'
  ,
  dependencies=[protos_dot_public_dot_common_dot_CommonService__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_JOBSTATUSENUM_JOBSTATUS = _descriptor.EnumDescriptor(
  name='JobStatus',
  full_name='ai.verta.modeldb.JobStatusEnum.JobStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT_STARTED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IN_PROGRESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=142,
  serialized_end=202,
)
_sym_db.RegisterEnumDescriptor(_JOBSTATUSENUM_JOBSTATUS)

_JOBTYPEENUM_JOBTYPE = _descriptor.EnumDescriptor(
  name='JobType',
  full_name='ai.verta.modeldb.JobTypeEnum.JobType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='KUBERNETES_JOB', index=0, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=219,
  serialized_end=248,
)
_sym_db.RegisterEnumDescriptor(_JOBTYPEENUM_JOBTYPE)


_JOBSTATUSENUM = _descriptor.Descriptor(
  name='JobStatusEnum',
  full_name='ai.verta.modeldb.JobStatusEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _JOBSTATUSENUM_JOBSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=202,
)


_JOBTYPEENUM = _descriptor.Descriptor(
  name='JobTypeEnum',
  full_name='ai.verta.modeldb.JobTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _JOBTYPEENUM_JOBTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=204,
  serialized_end=248,
)


_JOB = _descriptor.Descriptor(
  name='Job',
  full_name='ai.verta.modeldb.Job',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ai.verta.modeldb.Job.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='ai.verta.modeldb.Job.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='ai.verta.modeldb.Job.start_time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='ai.verta.modeldb.Job.end_time', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='ai.verta.modeldb.Job.metadata', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='job_status', full_name='ai.verta.modeldb.Job.job_status', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='job_type', full_name='ai.verta.modeldb.Job.job_type', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owner', full_name='ai.verta.modeldb.Job.owner', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=251,
  serialized_end=507,
)


_CREATEJOB_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.modeldb.CreateJob.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job', full_name='ai.verta.modeldb.CreateJob.Response.job', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=747,
  serialized_end=793,
)

_CREATEJOB = _descriptor.Descriptor(
  name='CreateJob',
  full_name='ai.verta.modeldb.CreateJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='ai.verta.modeldb.CreateJob.description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='ai.verta.modeldb.CreateJob.start_time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='ai.verta.modeldb.CreateJob.end_time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='ai.verta.modeldb.CreateJob.metadata', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='job_status', full_name='ai.verta.modeldb.CreateJob.job_status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='job_type', full_name='ai.verta.modeldb.CreateJob.job_type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATEJOB_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=510,
  serialized_end=793,
)


_UPDATEJOB_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.modeldb.UpdateJob.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job', full_name='ai.verta.modeldb.UpdateJob.Response.job', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=747,
  serialized_end=793,
)

_UPDATEJOB = _descriptor.Descriptor(
  name='UpdateJob',
  full_name='ai.verta.modeldb.UpdateJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ai.verta.modeldb.UpdateJob.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='ai.verta.modeldb.UpdateJob.end_time', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='job_status', full_name='ai.verta.modeldb.UpdateJob.job_status', index=2,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATEJOB_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=796,
  serialized_end=948,
)


_DELETEJOB_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.modeldb.DeleteJob.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ai.verta.modeldb.DeleteJob.Response.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=975,
  serialized_end=1001,
)

_DELETEJOB = _descriptor.Descriptor(
  name='DeleteJob',
  full_name='ai.verta.modeldb.DeleteJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ai.verta.modeldb.DeleteJob.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DELETEJOB_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=950,
  serialized_end=1001,
)


_GETJOB_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.modeldb.GetJob.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job', full_name='ai.verta.modeldb.GetJob.Response.job', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=747,
  serialized_end=793,
)

_GETJOB = _descriptor.Descriptor(
  name='GetJob',
  full_name='ai.verta.modeldb.GetJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ai.verta.modeldb.GetJob.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETJOB_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1003,
  serialized_end=1071,
)

_JOBSTATUSENUM_JOBSTATUS.containing_type = _JOBSTATUSENUM
_JOBTYPEENUM_JOBTYPE.containing_type = _JOBTYPEENUM
_JOB.fields_by_name['metadata'].message_type = protos_dot_public_dot_common_dot_CommonService__pb2._KEYVALUE
_JOB.fields_by_name['job_status'].enum_type = _JOBSTATUSENUM_JOBSTATUS
_JOB.fields_by_name['job_type'].enum_type = _JOBTYPEENUM_JOBTYPE
_CREATEJOB_RESPONSE.fields_by_name['job'].message_type = _JOB
_CREATEJOB_RESPONSE.containing_type = _CREATEJOB
_CREATEJOB.fields_by_name['metadata'].message_type = protos_dot_public_dot_common_dot_CommonService__pb2._KEYVALUE
_CREATEJOB.fields_by_name['job_status'].enum_type = _JOBSTATUSENUM_JOBSTATUS
_CREATEJOB.fields_by_name['job_type'].enum_type = _JOBTYPEENUM_JOBTYPE
_UPDATEJOB_RESPONSE.fields_by_name['job'].message_type = _JOB
_UPDATEJOB_RESPONSE.containing_type = _UPDATEJOB
_UPDATEJOB.fields_by_name['job_status'].enum_type = _JOBSTATUSENUM_JOBSTATUS
_DELETEJOB_RESPONSE.containing_type = _DELETEJOB
_GETJOB_RESPONSE.fields_by_name['job'].message_type = _JOB
_GETJOB_RESPONSE.containing_type = _GETJOB
DESCRIPTOR.message_types_by_name['JobStatusEnum'] = _JOBSTATUSENUM
DESCRIPTOR.message_types_by_name['JobTypeEnum'] = _JOBTYPEENUM
DESCRIPTOR.message_types_by_name['Job'] = _JOB
DESCRIPTOR.message_types_by_name['CreateJob'] = _CREATEJOB
DESCRIPTOR.message_types_by_name['UpdateJob'] = _UPDATEJOB
DESCRIPTOR.message_types_by_name['DeleteJob'] = _DELETEJOB
DESCRIPTOR.message_types_by_name['GetJob'] = _GETJOB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JobStatusEnum = _reflection.GeneratedProtocolMessageType('JobStatusEnum', (_message.Message,), {
  'DESCRIPTOR' : _JOBSTATUSENUM,
  '__module__' : 'protos.public.modeldb.Job_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.JobStatusEnum)
  })
_sym_db.RegisterMessage(JobStatusEnum)

JobTypeEnum = _reflection.GeneratedProtocolMessageType('JobTypeEnum', (_message.Message,), {
  'DESCRIPTOR' : _JOBTYPEENUM,
  '__module__' : 'protos.public.modeldb.Job_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.JobTypeEnum)
  })
_sym_db.RegisterMessage(JobTypeEnum)

Job = _reflection.GeneratedProtocolMessageType('Job', (_message.Message,), {
  'DESCRIPTOR' : _JOB,
  '__module__' : 'protos.public.modeldb.Job_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.Job)
  })
_sym_db.RegisterMessage(Job)

CreateJob = _reflection.GeneratedProtocolMessageType('CreateJob', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _CREATEJOB_RESPONSE,
    '__module__' : 'protos.public.modeldb.Job_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.modeldb.CreateJob.Response)
    })
  ,
  'DESCRIPTOR' : _CREATEJOB,
  '__module__' : 'protos.public.modeldb.Job_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.CreateJob)
  })
_sym_db.RegisterMessage(CreateJob)
_sym_db.RegisterMessage(CreateJob.Response)

UpdateJob = _reflection.GeneratedProtocolMessageType('UpdateJob', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _UPDATEJOB_RESPONSE,
    '__module__' : 'protos.public.modeldb.Job_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.modeldb.UpdateJob.Response)
    })
  ,
  'DESCRIPTOR' : _UPDATEJOB,
  '__module__' : 'protos.public.modeldb.Job_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.UpdateJob)
  })
_sym_db.RegisterMessage(UpdateJob)
_sym_db.RegisterMessage(UpdateJob.Response)

DeleteJob = _reflection.GeneratedProtocolMessageType('DeleteJob', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _DELETEJOB_RESPONSE,
    '__module__' : 'protos.public.modeldb.Job_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.modeldb.DeleteJob.Response)
    })
  ,
  'DESCRIPTOR' : _DELETEJOB,
  '__module__' : 'protos.public.modeldb.Job_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.DeleteJob)
  })
_sym_db.RegisterMessage(DeleteJob)
_sym_db.RegisterMessage(DeleteJob.Response)

GetJob = _reflection.GeneratedProtocolMessageType('GetJob', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _GETJOB_RESPONSE,
    '__module__' : 'protos.public.modeldb.Job_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.modeldb.GetJob.Response)
    })
  ,
  'DESCRIPTOR' : _GETJOB,
  '__module__' : 'protos.public.modeldb.Job_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.GetJob)
  })
_sym_db.RegisterMessage(GetJob)
_sym_db.RegisterMessage(GetJob.Response)


DESCRIPTOR._options = None

_JOBSERVICE = _descriptor.ServiceDescriptor(
  name='JobService',
  full_name='ai.verta.modeldb.JobService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1074,
  serialized_end=1505,
  methods=[
  _descriptor.MethodDescriptor(
    name='createJob',
    full_name='ai.verta.modeldb.JobService.createJob',
    index=0,
    containing_service=None,
    input_type=_CREATEJOB,
    output_type=_CREATEJOB_RESPONSE,
    serialized_options=b'\202\323\344\223\002\026\"\021/v1/job/createJob:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='getJob',
    full_name='ai.verta.modeldb.JobService.getJob',
    index=1,
    containing_service=None,
    input_type=_GETJOB,
    output_type=_GETJOB_RESPONSE,
    serialized_options=b'\202\323\344\223\002\020\022\016/v1/job/getJob',
  ),
  _descriptor.MethodDescriptor(
    name='updateJob',
    full_name='ai.verta.modeldb.JobService.updateJob',
    index=2,
    containing_service=None,
    input_type=_UPDATEJOB,
    output_type=_UPDATEJOB_RESPONSE,
    serialized_options=b'\202\323\344\223\002\023\022\021/v1/job/updateJob',
  ),
  _descriptor.MethodDescriptor(
    name='deleteJob',
    full_name='ai.verta.modeldb.JobService.deleteJob',
    index=3,
    containing_service=None,
    input_type=_DELETEJOB,
    output_type=_DELETEJOB_RESPONSE,
    serialized_options=b'\202\323\344\223\002\023\022\021/v1/job/deleteJob',
  ),
])
_sym_db.RegisterServiceDescriptor(_JOBSERVICE)

DESCRIPTOR.services_by_name['JobService'] = _JOBSERVICE

# @@protoc_insertion_point(module_scope)
