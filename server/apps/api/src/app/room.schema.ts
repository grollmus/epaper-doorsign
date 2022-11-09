import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { HydratedDocument } from 'mongoose';

export type RoomDocument = HydratedDocument<Room>;

@Schema()
export class Room {
  @Prop()
  name: string;
}

export const RoomDocument = SchemaFactory.createForClass(Room);
