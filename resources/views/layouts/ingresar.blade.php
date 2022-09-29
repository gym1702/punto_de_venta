@extends('layouts.admin')

<!-- content para cuando aun no inicia sesion -->
@section('content')

<div class="hold-transition login-page">
    <div class="login-box">
        <div class="card card-outline card-primary">
            <div class="card-header text-center">
                <a href="#" class="h1"><b>Ventas</b>RGR</a>
            </div>
            <div class="card-body">
                <p class="login-box-msg">Bienvenido</p>

                <form action="{{ route('login') }}" method="post">
                    @csrf
                    <div class="input-group mb-3">
                        <input type="email" name="email" class="form-control" required value="" placeholder="Email">
                        <div class="input-group-append">
                            <div class="input-group-text">
                                <span class="fas fa-envelope"></span>
                            </div>
                        </div>
                    </div>

                    <div class="input-group mb-3">
                    <input type="password" name="password" class="form-control" required value="" placeholder="Contraseña">
                        <div class="input-group-append">
                            <div class="input-group-text">
                                <span class="fas fa-lock"></span>
                            </div>
                        </div>
                    </div>

                    <div class="text-center mt-2 mb-3">
                        <div class="col-xs-12">
                            <button type="submit" class="btn btn-primary btn-block btn-flat">Ingresar</button>
                        </div>
                    </div>                    
                </form>                
            </div>
        </div>
    </div>
</div>
@endsection