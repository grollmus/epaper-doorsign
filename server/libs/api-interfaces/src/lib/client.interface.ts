import { Database } from "./_database.interface";

export interface Client extends Database {
  name: string;
  tag: string;
}
