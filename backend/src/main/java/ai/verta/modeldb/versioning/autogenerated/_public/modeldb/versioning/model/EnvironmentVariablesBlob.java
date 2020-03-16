// THIS FILE IS AUTO-GENERATED. DO NOT EDIT
package ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model;

import ai.verta.modeldb.ModelDBException;
import ai.verta.modeldb.versioning.*;
import ai.verta.modeldb.versioning.blob.diff.Function3;
import ai.verta.modeldb.versioning.blob.diff.ProtoType;
import ai.verta.modeldb.versioning.blob.visitors.Visitor;
import java.util.*;
import java.util.function.Function;

public class EnvironmentVariablesBlob implements ProtoType {
  public String Name;
  public String Value;

  public EnvironmentVariablesBlob() {
    this.Name = null;
    this.Value = null;
  }

  public Boolean isEmpty() {
    if (this.Name != null) {
      return false;
    }
    if (this.Value != null) {
      return false;
    }
    return true;
  }

  // TODO: not consider order on lists
  public Boolean equals(EnvironmentVariablesBlob other) {
    if (other == null) {
      return false;
    }
    {
      Function3<String, String, Boolean> f = (x, y) -> x.equals(y);
      if (this.Name != null || other.Name != null) {
        if (this.Name == null && other.Name != null) return false;
        if (this.Name != null && other.Name == null) return false;
        if (!f.apply(this.Name, other.Name)) return false;
      }
    }
    {
      Function3<String, String, Boolean> f = (x, y) -> x.equals(y);
      if (this.Value != null || other.Value != null) {
        if (this.Value == null && other.Value != null) return false;
        if (this.Value != null && other.Value == null) return false;
        if (!f.apply(this.Value, other.Value)) return false;
      }
    }
    return true;
  }

  public EnvironmentVariablesBlob setName(String value) {
    this.Name = value;
    return this;
  }

  public EnvironmentVariablesBlob setValue(String value) {
    this.Value = value;
    return this;
  }

  public static EnvironmentVariablesBlob fromProto(
      ai.verta.modeldb.versioning.EnvironmentVariablesBlob blob) {
    if (blob == null) {
      return null;
    }

    EnvironmentVariablesBlob obj = new EnvironmentVariablesBlob();
    {
      Function<ai.verta.modeldb.versioning.EnvironmentVariablesBlob, String> f =
          x -> (blob.getName());
      obj.Name = f.apply(blob);
    }
    {
      Function<ai.verta.modeldb.versioning.EnvironmentVariablesBlob, String> f =
          x -> (blob.getValue());
      obj.Value = f.apply(blob);
    }
    return obj;
  }

  public ai.verta.modeldb.versioning.EnvironmentVariablesBlob.Builder toProto() {
    ai.verta.modeldb.versioning.EnvironmentVariablesBlob.Builder builder =
        ai.verta.modeldb.versioning.EnvironmentVariablesBlob.newBuilder();
    {
      if (this.Name != null) {
        Function<ai.verta.modeldb.versioning.EnvironmentVariablesBlob.Builder, Void> f =
            x -> {
              builder.setName(this.Name);
              return null;
            };
        f.apply(builder);
      }
    }
    {
      if (this.Value != null) {
        Function<ai.verta.modeldb.versioning.EnvironmentVariablesBlob.Builder, Void> f =
            x -> {
              builder.setValue(this.Value);
              return null;
            };
        f.apply(builder);
      }
    }
    return builder;
  }

  public void preVisitShallow(Visitor visitor) throws ModelDBException {
    visitor.preVisitEnvironmentVariablesBlob(this);
  }

  public void preVisitDeep(Visitor visitor) throws ModelDBException {
    this.preVisitShallow(visitor);
    visitor.preVisitDeepString(this.Name);
    visitor.preVisitDeepString(this.Value);
  }

  public EnvironmentVariablesBlob postVisitShallow(Visitor visitor) throws ModelDBException {
    return visitor.postVisitEnvironmentVariablesBlob(this);
  }

  public EnvironmentVariablesBlob postVisitDeep(Visitor visitor) throws ModelDBException {
    this.Name = visitor.postVisitDeepString(this.Name);
    this.Value = visitor.postVisitDeepString(this.Value);
    return this.postVisitShallow(visitor);
  }
}
