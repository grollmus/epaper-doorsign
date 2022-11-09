import { Model, Types } from 'mongoose';
import { Injectable, Logger } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Client, ClientDocument } from './client.schema';
import { CreateClientDto } from './client.dto';

@Injectable()
export class ClientService {
  private readonly logger = new Logger(ClientService.name);

  constructor(
    @InjectModel(Client.name) private clientModel: Model<ClientDocument>
  ) {}

  async create(createClientDto: CreateClientDto): Promise<Client> {
    const clientWithTag = await this.findOneByTag(createClientDto.tag)

    if (clientWithTag === null)
      return new this.clientModel(createClientDto).save();
    else
      return clientWithTag
  }

  async findAll(): Promise<Client[]> {
    return this.clientModel.find().exec();
  }

  async findOneById(_id: Types.ObjectId): Promise<Client> {
    return this.clientModel.findOne(_id);
  }

  async findOneByTag(tag: string): Promise<Client> {
    return this.clientModel.findOne({ tag });
  }
}
