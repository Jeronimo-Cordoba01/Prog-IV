import { Module } from '@nestjs/common';
import { AutenticationModule } from './autentication/autentication.module';
import { MongooseModule } from '@nestjs/mongoose/dist/mongoose.module';
import { ConfigModule } from '@nestjs/config/dist/config.module';

@Module({
  imports: [
    ConfigModule.forRoot(),
    AutenticationModule, 
    MongooseModule.forRoot(process.env.MONGO_URI!), ],
  controllers: [],
  providers: [],
})
export class AppModule {}
