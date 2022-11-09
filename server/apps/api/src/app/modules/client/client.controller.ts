import { Body, Controller, Get, Post } from '@nestjs/common';
import { CreateClientDto } from './client.dto';
import { ClientService } from './client.service';

@Controller('client')
export class ClientController {
  constructor(private readonly clientService: ClientService) {}

  @Get()
  async getClientList() {
    return this.clientService.findAll();
  }

  @Post('register')
  async registerClient(@Body() createClientDto: CreateClientDto) {
    return this.clientService.create(createClientDto);
  }
}
