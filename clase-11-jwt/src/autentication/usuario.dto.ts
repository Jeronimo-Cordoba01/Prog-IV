import { IsString } from "class-validator";

export class UsuarioRegistroDto {
    @IsString()
    nombre: string;
    @IsString()
    email: string;
    @IsString()
    password: string;
}

export class UsuarioLoginDto {
    @IsString()
    email: string;
    @IsString()
    password: string;
}