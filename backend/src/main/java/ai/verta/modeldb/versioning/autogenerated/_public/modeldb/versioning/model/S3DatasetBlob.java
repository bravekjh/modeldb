// THIS FILE IS AUTO-GENERATED. DO NOT EDIT
package ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model;

import ai.verta.modeldb.ModelDBException;
import ai.verta.modeldb.versioning.*;
import ai.verta.modeldb.versioning.blob.diff.Function3;
import ai.verta.modeldb.versioning.blob.diff.ProtoType;
import ai.verta.modeldb.versioning.blob.visitors.Visitor;
import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class S3DatasetBlob implements ProtoType {
  public List<S3DatasetComponentBlob> Components;

  public S3DatasetBlob() {
    this.Components = null;
  }

  public Boolean isEmpty() {
    if (this.Components != null) {
      return false;
    }
    return true;
  }

  // TODO: not consider order on lists
  public Boolean equals(S3DatasetBlob other) {
    if (other == null) {
      return false;
    }
    {
      Function3<List<S3DatasetComponentBlob>, List<S3DatasetComponentBlob>, Boolean> f =
          (x2, y2) ->
              IntStream.range(0, Math.min(x2.size(), y2.size()))
                  .mapToObj(
                      i -> {
                        Function3<S3DatasetComponentBlob, S3DatasetComponentBlob, Boolean> f2 =
                            (x, y) -> x.equals(y);
                        return f2.apply(x2.get(i), y2.get(i));
                      })
                  .filter(x -> x != null)
                  .collect(Collectors.toList())
                  .isEmpty();
      if (this.Components != null || other.Components != null) {
        if (this.Components == null && other.Components != null) return false;
        if (this.Components != null && other.Components == null) return false;
        if (!f.apply(this.Components, other.Components)) return false;
      }
    }
    return true;
  }

  public S3DatasetBlob setComponents(List<S3DatasetComponentBlob> value) {
    this.Components = value;
    return this;
  }

  public static S3DatasetBlob fromProto(ai.verta.modeldb.versioning.S3DatasetBlob blob) {
    if (blob == null) {
      return null;
    }

    S3DatasetBlob obj = new S3DatasetBlob();
    {
      Function<ai.verta.modeldb.versioning.S3DatasetBlob, List<S3DatasetComponentBlob>> f =
          x ->
              blob.getComponentsList().stream()
                  .map(S3DatasetComponentBlob::fromProto)
                  .collect(Collectors.toList());
      obj.Components = f.apply(blob);
    }
    return obj;
  }

  public ai.verta.modeldb.versioning.S3DatasetBlob.Builder toProto() {
    ai.verta.modeldb.versioning.S3DatasetBlob.Builder builder =
        ai.verta.modeldb.versioning.S3DatasetBlob.newBuilder();
    {
      if (this.Components != null) {
        Function<ai.verta.modeldb.versioning.S3DatasetBlob.Builder, Void> f =
            x -> {
              builder.addAllComponents(
                  this.Components.stream()
                      .map(y -> y.toProto().build())
                      .collect(Collectors.toList()));
              return null;
            };
        f.apply(builder);
      }
    }
    return builder;
  }

  public void preVisitShallow(Visitor visitor) throws ModelDBException {
    visitor.preVisitS3DatasetBlob(this);
  }

  public void preVisitDeep(Visitor visitor) throws ModelDBException {
    this.preVisitShallow(visitor);
    visitor.preVisitDeepListOfS3DatasetComponentBlob(this.Components);
  }

  public S3DatasetBlob postVisitShallow(Visitor visitor) throws ModelDBException {
    return visitor.postVisitS3DatasetBlob(this);
  }

  public S3DatasetBlob postVisitDeep(Visitor visitor) throws ModelDBException {
    this.Components = visitor.postVisitDeepListOfS3DatasetComponentBlob(this.Components);
    return this.postVisitShallow(visitor);
  }
}
