import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';

import { AppController } from './app.controller';
import { AppService } from './app.service';
import { ClientModule } from './modules';

@Module({
  imports: [ClientModule, MongooseModule.forRoot('mongodb://localhost/roomserver')],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
