// THIS FILE IS AUTO-GENERATED. DO NOT EDIT
package ai.verta.swagger._public.modeldb.versioning.model

import scala.util.Try

import net.liftweb.json._

import ai.verta.swagger._public.modeldb.versioning.model.ArtifactTypeEnumArtifactType._
import ai.verta.swagger._public.modeldb.versioning.model.DiffStatusEnumDiffStatus._
import ai.verta.swagger._public.modeldb.versioning.model.OperatorEnumOperator._
import ai.verta.swagger._public.modeldb.versioning.model.ProtobufNullValue._
import ai.verta.swagger._public.modeldb.versioning.model.RepositoryVisibilityEnumRepositoryVisibility._
import ai.verta.swagger._public.modeldb.versioning.model.TernaryEnumTernary._
import ai.verta.swagger._public.modeldb.versioning.model.ValueTypeEnumValueType._
import ai.verta.swagger._public.modeldb.versioning.model.VersioningBlobType._
import ai.verta.swagger._public.modeldb.versioning.model.WorkspaceTypeEnumWorkspaceType._
import ai.verta.swagger.client.objects._

case class VersioningGetCommitComponentRequestResponse (
  blob: Option[VersioningBlob] = None,
  folder: Option[VersioningFolder] = None
) extends BaseSwagger {
  def toJson(): JValue = VersioningGetCommitComponentRequestResponse.toJson(this)
}

object VersioningGetCommitComponentRequestResponse {
  def toJson(obj: VersioningGetCommitComponentRequestResponse): JObject = {
    new JObject(
      List[Option[JField]](
        obj.blob.map(x => JField("blob", ((x: VersioningBlob) => VersioningBlob.toJson(x))(x))),
        obj.folder.map(x => JField("folder", ((x: VersioningFolder) => VersioningFolder.toJson(x))(x)))
      ).flatMap(x => x match {
        case Some(y) => List(y)
        case None => Nil
      })
    )
  }

  def fromJson(value: JValue): VersioningGetCommitComponentRequestResponse =
    value match {
      case JObject(fields) => {
        val fieldsMap = fields.map(f => (f.name, f.value)).toMap
        VersioningGetCommitComponentRequestResponse(
          // TODO: handle required
          blob = fieldsMap.get("blob").map(VersioningBlob.fromJson),
          folder = fieldsMap.get("folder").map(VersioningFolder.fromJson)
        )
      }
      case _ => throw new IllegalArgumentException(s"unknown type ${value.getClass.toString}")
    }
}
