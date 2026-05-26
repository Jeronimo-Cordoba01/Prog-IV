import { Body, Controller, Get, Post, Req, UseGuards } from '@nestjs/common';
import { AutenticationService } from './autentication.service';
import { UsuarioLoginDto, UsuarioRegistroDto } from './usuario.dto';
import { TokenGuard } from './token/token.guard';
import { Request } from 'express';

@Controller('autentication')
export class AutenticationController {
  constructor(private readonly autenticationService: AutenticationService) {}

  @Post('/registro')
  registrar(@Body() usuario: UsuarioRegistroDto) {
    return this.autenticationService.registrar(usuario);
  }

  @Post('/ingresar')
  ingresar(@Body() usuario: UsuarioLoginDto) {
    return this.autenticationService.ingresar(usuario);
  }

  @Get('/seguro')
  @UseGuards(TokenGuard)
  rutaSegura(@Body('emailDelToken') email: any) {
    console.log(email);
    // SOLO Voy a poder acceder si tengo unt tóken válido

    return { mensaje: 'Acceso otorgado a ' + email };
  }
}