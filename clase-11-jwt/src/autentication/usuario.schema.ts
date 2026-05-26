import {Schema, Prop, SchemaFactory} from '@nestjs/mongoose';

@Schema()
export class Usuario {
    @Prop()
    nombre: string;
    @Prop()
    email: string;
    @Prop()
    password: string;
}

export const UsuarioSchema = SchemaFactory.createForClass(Usuario);