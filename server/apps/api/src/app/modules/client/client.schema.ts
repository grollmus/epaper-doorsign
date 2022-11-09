
import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import mongoose, { HydratedDocument } from 'mongoose';

export type ClientDocument = HydratedDocument<Client>;

@Schema()
export class Client {
  @Prop({ required: true })
  name: string;

  @Prop({ unique: true, required: true })
  tag: string;
}

export const ClientSchema = SchemaFactory.createForClass(Client);
