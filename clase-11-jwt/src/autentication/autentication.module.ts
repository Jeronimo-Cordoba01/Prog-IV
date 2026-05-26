import { Module } from '@nestjs/common';
import { AutenticationService } from './autentication.service';
import { AutenticationController } from './autentication.controller';
import { Usuario, UsuarioSchema } from './usuario.schema';
import { MongooseModule } from '@nestjs/mongoose/dist/mongoose.module';

@Module({
  imports: [MongooseModule.forFeature([{name: Usuario.name, schema: UsuarioSchema}])],
  controllers: [AutenticationController],
  providers: [AutenticationService],
})
export class AutenticationModule {}
