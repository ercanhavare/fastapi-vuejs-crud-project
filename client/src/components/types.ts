/**
 * Hero interface representing the structure of a hero object
 * This interface defines the properties that a hero object can have, including optional properties for age and secret name.
 */
export interface Hero {
  id: number;
  name: string;
  age?: number;
  secret_name?: string;
}