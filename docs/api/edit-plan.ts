// EditPlan 1.0 reference types. JSON Schema remains the source of truth.
export type TechnicalEvidence = { skill_id: string; version: `${number}.${number}.${number}` };

export interface RemasterParameters {
  brightness: number;
  contrast: number;
  highlights: number;
  shadows: number;
  saturation: number;
  temperature: number;
  tint: number;
  sharpness: number;
  denoise: number;
  vignette: number;
}

export interface LutParameters {
  lut_id: string;
  strength: number;
  interpolation: "trilinear";
  preserve_luminance: boolean;
}

export interface GenerateAIParameters {
  operation: "edit";
  use_case:
    | "text-localization"
    | "identity-preserve"
    | "precise-object-edit"
    | "lighting-weather"
    | "background-extraction"
    | "style-transfer"
    | "compositing"
    | "sketch-to-render";
  execution_mode: "openai-image-api";
  prompt: string;
  constraints: string[];
  avoid: string[];
  output_format: "png";
}

export type EditStep =
  | { order: number; tool: "remaster"; parameters: RemasterParameters; reason_ko: string; evidence: TechnicalEvidence[] }
  | { order: number; tool: "lut"; parameters: LutParameters; reason_ko: string; evidence: TechnicalEvidence[] }
  | { order: number; tool: "generate_ai"; parameters: GenerateAIParameters; reason_ko: string; evidence: TechnicalEvidence[] };

export interface EditPlan {
  schema_version: "1.0";
  request_id: string;
  summary_ko: string;
  steps: EditStep[];
  overall_reason_ko: string;
  confidence: number;
  warnings_ko: string[];
}

export interface ApiError {
  code: string;
  message_ko: string;
  retryable: boolean;
}

export interface ApiMeta {
  created_at: string;
  expires_at: string | null;
}

export interface Envelope<T> {
  data: T | null;
  error: ApiError | null;
  meta: ApiMeta;
}

export interface UploadRequestBody {
  filename: string;
  mime: "image/jpeg" | "image/png" | "image/webp";
  byte_size: number;
  sha256?: string | null;
}

export interface UploadRequestData {
  asset_id: string;
  upload_url: string;
  upload_method: "PUT";
  expires_at: string;
}

export interface UploadStatusData {
  asset_id: string;
  status: "uploaded";
}

export interface ClientCapabilities {
  edit_plan_version: "1.0";
  remaster_engine_version: "1.0";
  lut_catalog_version: string;
}

export interface EditRequestBody {
  schema_version: "1.0";
  client_request_id: string;
  asset_id: string;
  prompt: string;
  locale: "ko-KR";
  client_capabilities: ClientCapabilities;
}

export type EditRequestStatus = "queued" | "analyzing" | "completed" | "failed";

export interface EditAcceptedData {
  request_id: string;
  status: EditRequestStatus;
  status_url: string;
}

export interface EditStatusData {
  request_id: string;
  status: EditRequestStatus;
  plan: EditPlan | null;
}

export interface ServiceCapabilitiesData {
  planner: "hermes-llm";
  edit_plan_versions: "1.0"[];
  remaster_engine_versions: "1.0"[];
  imagegen_execution_modes: "openai-image-api"[];
  upload_mime_types: ("image/jpeg" | "image/png" | "image/webp")[];
  swagger_url: "/docs";
  redoc_url: "/redoc";
  openapi_url: "/openapi.json";
}
