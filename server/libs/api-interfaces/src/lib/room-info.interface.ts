import { RoomBooking } from "./room-booking.interface";

export interface RoomInfo {
  roomName: string;
  bookings: RoomBooking[];
}
