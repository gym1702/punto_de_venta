<div class="modal fade" id="modalEditar{{$item->id}}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Editar categoría</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>

      <div class="modal-body">
        <form action="{{route('categories.update', $item->id) }}" role="form" method="POST" id="editarCategoriaFrm">
            
            @method('PUT')
            @csrf
            
            <div class="row">
                <div class="col-4">
                    <label for="nombre">Nombre</label>
                    <input type="text" name="nombre" id="nombre" value="{{ $item->nombre }}" class="form-control" placeholder="Nombre" required>
                </div>
                <div class="col-8">
                    <label for="descripcion">Descripción</label>
                    <input type="text" name="descripcion" id="descripcion" value="{{ $item->descripcion }}" value="" class="form-control" placeholder="Descripción">
                </div>
            </div>
            <br>
            <hr>

            <div align="right">
                <button type="submit" class="btn btn-primary">Actualizar</button>

                <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancelar</button>
          </div>

        </form>
      </div>
    </div>
  </div>
</div>