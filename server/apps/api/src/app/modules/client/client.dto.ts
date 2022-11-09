import { ApiProperty } from '@nestjs/swagger';
import { IsString } from 'class-validator';

export class CreateClientDto {
  @IsString()
  @ApiProperty({ default: 'Zugspitze' })
  readonly name: string;

  @IsString()
  @ApiProperty({ default: 'og-2-zugspitze' })
  readonly tag: string;
}
