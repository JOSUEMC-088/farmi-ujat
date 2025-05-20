from pyairtable.orm import Model
from pyairtable.orm import fields as f


class Receta(Model):
    medicamento = f.TextField("medicamento")
    interacciones = f.TextField("interacciones")

    class Meta:
        api_key = "patekCShAWSQq4Krd.4d248f4b7187fe3a7e38f2303d0673215574e4d3b583e0cdaaf79f189c75257e"
        base_id = "appHe17ks4bpkBHBC"
        table_name=("receta")

