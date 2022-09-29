<div class="modal fade" id="modalCrear" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Crear categoría</h5>
        <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>

      <div class="modal-body">
        <form action="{{route('categories.store')}}" role="form" method="POST" id="crearCategoriaFrm">
          
          @csrf
    
          <div class="row">
            <div class="col-4">
                <label for="nombre">Nombre</label>
                <input type="text" name="nombre" id="nombre" class="form-control" placeholder="Nombre" required>
            </div>
            <div class="col-8">
                <label for="descripcion">Descripción</label>
                <input type="text" name="descripcion" id="descripcion" class="form-control" placeholder="Descripción">
            </div>
          </div>
          <br>
          <hr>

          <div align="right">
            <button type="submit" class="btn btn-primary">Guardar</button>

            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
          </div>

        </form>
      </div>

      
    </div>
  </div>
</div>
