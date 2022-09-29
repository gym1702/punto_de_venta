@extends('layouts.admin')
@section('titulo', 'Gestion de categorias')

<!-- SECCION CONTENIDO PARA USUARIOS AUTENTICADOS -->
@section('contenido') 
<section class="content-wrapper">
    
    <div class="content-header">
      <div class="container-fluid">
        <div class="row mb-2">
          <div class="col-sm-6">
            <h1 class="m-0">Gestor de Categorias</h1>
          </div>
        </div>
      </div>
    </div>  
        
    <div class="container-fluid">
        <div class="card">

            <div class="box-header mb-2 mt-3 ml-4">
                <a href="" data-toggle="modal" data-target="#modalCrear" class="btn btn-primary" type="button">Agregar</a>
            </div>

            <div class="card-body">

                <table class="table table-bordered table-hover table-striped" id="tbl" >
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Nombre</th>
                            <th>Descripcion</th>

                            <th>Acciones</th>
                        </tr>
                    </thead>

                    <tbody>

                        @foreach ($categories as $item)
                            <tr>
                                <th scope="row">{{ $item->id }}</th>
                                <td>
                                    <a href="{{route('categories.show', $item)}}">{{ $item->nombre }}</a>
                                </td>
                                <td>{{ $item->descripcion }}</td>

                                <td>
                                    
                                    <a href="" data-toggle="modal" data-target="#modalEditar{{$item->id}}" title="Editar" class="btn btn-info btn-sm">
                                        <i class="fa fa-edit"></i>
                                    </a>
                                                            
                                    <button title="Eliminar" type="submit" class="btn btn-danger btn-sm Eliminar" id="{{$item->id}}">
                                        <i class="fa fa-trash-alt"></i>
                                    </button>
                                   
                                </td>
                            </tr>

                            @include('admin.categorias.modalCrear')
                            @include('admin.categorias.modalEditar')
                            
                        @endforeach

                    </tbody>
                </table>
            </div>

        </div>
    </div>

</section>
@endsection


@section('scripts')
    <script>
        //INICIALIZAR DATATABLE
        $("#tbl").DataTable({
            "responsive": true, 
            "lengthChange": false, 
            "autoWidth": false, 
            "language": {
                    "decimal": "",
                    "emptyTable": "No hay información",
                    "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                    "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
                    "infoFiltered": "(Filtrado de _MAX_ total entradas)",
                    "infoPostFix": "",
                    "thousands": ",",
                    "lengthMenu": "Mostrar _MENU_ Entradas",
                    "loadingRecords": "Cargando...",
                    "processing": "Procesando...",
                    "search": "Buscar:",
                    "zeroRecords": "Sin resultados encontrados",
                    "paginate": {
                        "first": "Primero",
                        "last": "Ultimo",
                        "next": "Siguiente",
                        "previous": "Anterior"
                    },
                },
            // "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
            "buttons": [
                {
                    extend: 'excelHtml5',
                    text: '<i class="fas fa-file-excel"></i>',
                    titleAttr: 'Exportar a Excel',
                    className: 'btn btn-success',
                    title:     'Listado de categorias',
                    exportOptions: {
                        columns: [0,1]
                    }
                },
                {
                    extend: 'pdfHtml5',
                    text: '<i class="fas fa-file-pdf"></i>',
                    titleAttr: 'Exportar a PDF',
                    className: 'btn btn-danger',
                    title:     'Listado de categorias',
                    exportOptions: {
                        columns: [0,1]
                    }
                },
                {
                    extend: 'print',
                    text: '<i class="fas fa-print"></i>',
                    titleAttr: 'Imprimir',
                    className: 'btn btn-info',
                    title:     'Listado de categorias',
                    exportOptions: {
                        columns: [0,1]
                    }
                },
                {
                    extend: 'colvis',
                    text: '<i class="fas fa-table"></i>',
                    titleAttr: 'Mostar/ocultar campos',
                    className: 'btn btn-secondary'
                },

            ]
        }).buttons().container().appendTo('#tbl_wrapper .col-md-6:eq(0)');  
    </script>


    <!-- MENSAJES SWEETALERT DE ELIMINACION -->
    <script type="text/javascript">
        $('#tbl').on('click', '.Eliminar', function(){

        var id = $(this).attr("id");

        Swal.fire({
            title:'¿Esta seguro de querer eliminar la categoria con el id: '+id+'?',
            icon: 'question',
            showCancelButton: true,
            cancelButtonText: 'Cancelar',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Eliminar',
            confirmButtonColor: '#3085d6'

            }).then((result) => {
                if(result.isConfirmed){
                    window.location = 'Eliminar-Categoria/'+id;
                }
            })
        })
    </script>
    
@endsection
