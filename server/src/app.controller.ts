import { Controller, Get } from '@nestjs/common';
import { AppService } from './app.service';
import { RoomInfo } from './interfaces';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): RoomInfo {
    return this.appService.dummyRoomData();
  }
}
