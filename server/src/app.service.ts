import { Injectable } from '@nestjs/common';
import { dummyRoomInfoData } from './data/dummy-room-info.data';
import { RoomInfo } from './interfaces';

@Injectable()
export class AppService {
  dummyRoomData(): RoomInfo {
    return dummyRoomInfoData;
  }
}
