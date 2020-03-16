// THIS FILE IS AUTO-GENERATED. DO NOT EDIT
package ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model;

import ai.verta.modeldb.ModelDBException;
import ai.verta.modeldb.versioning.*;
import ai.verta.modeldb.versioning.blob.diff.Function3;
import ai.verta.modeldb.versioning.blob.diff.ProtoType;
import ai.verta.modeldb.versioning.blob.visitors.Visitor;
import java.util.*;
import java.util.function.Function;

public class PathDatasetComponentBlob implements ProtoType {
  public String Path;
  public Long Size;
  public Long LastModifiedAtSource;
  public String Sha256;
  public String Md5;

  public PathDatasetComponentBlob() {
    this.Path = null;
    this.Size = 0l;
    this.LastModifiedAtSource = 0l;
    this.Sha256 = null;
    this.Md5 = null;
  }

  public Boolean isEmpty() {
    if (this.Path != null) {
      return false;
    }
    if (this.Size != null) {
      return false;
    }
    if (this.LastModifiedAtSource != null) {
      return false;
    }
    if (this.Sha256 != null) {
      return false;
    }
    if (this.Md5 != null) {
      return false;
    }
    return true;
  }

  // TODO: not consider order on lists
  public Boolean equals(PathDatasetComponentBlob other) {
    if (other == null) {
      return false;
    }
    {
      Function3<String, String, Boolean> f = (x, y) -> x.equals(y);
      if (this.Path != null || other.Path != null) {
        if (this.Path == null && other.Path != null) return false;
        if (this.Path != null && other.Path == null) return false;
        if (!f.apply(this.Path, other.Path)) return false;
      }
    }
    {
      Function3<Long, Long, Boolean> f = (x, y) -> x == y;
      if (this.Size != null || other.Size != null) {
        if (this.Size == null && other.Size != null) return false;
        if (this.Size != null && other.Size == null) return false;
        if (!f.apply(this.Size, other.Size)) return false;
      }
    }
    {
      Function3<Long, Long, Boolean> f = (x, y) -> x == y;
      if (this.LastModifiedAtSource != null || other.LastModifiedAtSource != null) {
        if (this.LastModifiedAtSource == null && other.LastModifiedAtSource != null) return false;
        if (this.LastModifiedAtSource != null && other.LastModifiedAtSource == null) return false;
        if (!f.apply(this.LastModifiedAtSource, other.LastModifiedAtSource)) return false;
      }
    }
    {
      Function3<String, String, Boolean> f = (x, y) -> x.equals(y);
      if (this.Sha256 != null || other.Sha256 != null) {
        if (this.Sha256 == null && other.Sha256 != null) return false;
        if (this.Sha256 != null && other.Sha256 == null) return false;
        if (!f.apply(this.Sha256, other.Sha256)) return false;
      }
    }
    {
      Function3<String, String, Boolean> f = (x, y) -> x.equals(y);
      if (this.Md5 != null || other.Md5 != null) {
        if (this.Md5 == null && other.Md5 != null) return false;
        if (this.Md5 != null && other.Md5 == null) return false;
        if (!f.apply(this.Md5, other.Md5)) return false;
      }
    }
    return true;
  }

  public PathDatasetComponentBlob setPath(String value) {
    this.Path = value;
    return this;
  }

  public PathDatasetComponentBlob setSize(Long value) {
    this.Size = value;
    return this;
  }

  public PathDatasetComponentBlob setLastModifiedAtSource(Long value) {
    this.LastModifiedAtSource = value;
    return this;
  }

  public PathDatasetComponentBlob setSha256(String value) {
    this.Sha256 = value;
    return this;
  }

  public PathDatasetComponentBlob setMd5(String value) {
    this.Md5 = value;
    return this;
  }

  public static PathDatasetComponentBlob fromProto(
      ai.verta.modeldb.versioning.PathDatasetComponentBlob blob) {
    if (blob == null) {
      return null;
    }

    PathDatasetComponentBlob obj = new PathDatasetComponentBlob();
    {
      Function<ai.verta.modeldb.versioning.PathDatasetComponentBlob, String> f =
          x -> (blob.getPath());
      obj.Path = f.apply(blob);
    }
    {
      Function<ai.verta.modeldb.versioning.PathDatasetComponentBlob, Long> f =
          x -> (blob.getSize());
      obj.Size = f.apply(blob);
    }
    {
      Function<ai.verta.modeldb.versioning.PathDatasetComponentBlob, Long> f =
          x -> (blob.getLastModifiedAtSource());
      obj.LastModifiedAtSource = f.apply(blob);
    }
    {
      Function<ai.verta.modeldb.versioning.PathDatasetComponentBlob, String> f =
          x -> (blob.getSha256());
      obj.Sha256 = f.apply(blob);
    }
    {
      Function<ai.verta.modeldb.versioning.PathDatasetComponentBlob, String> f =
          x -> (blob.getMd5());
      obj.Md5 = f.apply(blob);
    }
    return obj;
  }

  public ai.verta.modeldb.versioning.PathDatasetComponentBlob.Builder toProto() {
    ai.verta.modeldb.versioning.PathDatasetComponentBlob.Builder builder =
        ai.verta.modeldb.versioning.PathDatasetComponentBlob.newBuilder();
    {
      if (this.Path != null) {
        Function<ai.verta.modeldb.versioning.PathDatasetComponentBlob.Builder, Void> f =
            x -> {
              builder.setPath(this.Path);
              return null;
            };
        f.apply(builder);
      }
    }
    {
      if (this.Size != null) {
        Function<ai.verta.modeldb.versioning.PathDatasetComponentBlob.Builder, Void> f =
            x -> {
              builder.setSize(this.Size);
              return null;
            };
        f.apply(builder);
      }
    }
    {
      if (this.LastModifiedAtSource != null) {
        Function<ai.verta.modeldb.versioning.PathDatasetComponentBlob.Builder, Void> f =
            x -> {
              builder.setLastModifiedAtSource(this.LastModifiedAtSource);
              return null;
            };
        f.apply(builder);
      }
    }
    {
      if (this.Sha256 != null) {
        Function<ai.verta.modeldb.versioning.PathDatasetComponentBlob.Builder, Void> f =
            x -> {
              builder.setSha256(this.Sha256);
              return null;
            };
        f.apply(builder);
      }
    }
    {
      if (this.Md5 != null) {
        Function<ai.verta.modeldb.versioning.PathDatasetComponentBlob.Builder, Void> f =
            x -> {
              builder.setMd5(this.Md5);
              return null;
            };
        f.apply(builder);
      }
    }
    return builder;
  }

  public void preVisitShallow(Visitor visitor) throws ModelDBException {
    visitor.preVisitPathDatasetComponentBlob(this);
  }

  public void preVisitDeep(Visitor visitor) throws ModelDBException {
    this.preVisitShallow(visitor);
    visitor.preVisitDeepString(this.Path);
    visitor.preVisitDeepLong(this.Size);
    visitor.preVisitDeepLong(this.LastModifiedAtSource);
    visitor.preVisitDeepString(this.Sha256);
    visitor.preVisitDeepString(this.Md5);
  }

  public PathDatasetComponentBlob postVisitShallow(Visitor visitor) throws ModelDBException {
    return visitor.postVisitPathDatasetComponentBlob(this);
  }

  public PathDatasetComponentBlob postVisitDeep(Visitor visitor) throws ModelDBException {
    this.Path = visitor.postVisitDeepString(this.Path);
    this.Size = visitor.postVisitDeepLong(this.Size);
    this.LastModifiedAtSource = visitor.postVisitDeepLong(this.LastModifiedAtSource);
    this.Sha256 = visitor.postVisitDeepString(this.Sha256);
    this.Md5 = visitor.postVisitDeepString(this.Md5);
    return this.postVisitShallow(visitor);
  }
}
